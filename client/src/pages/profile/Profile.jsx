import { Link } from "react-router-dom";
import useAuth from "../../hooks/useAuth.js";
import path from "../../constants/path.js";

const Profile = () => {
  const { user } = useAuth();
  const initials = `${user?.username?.[0] || "U"}`.toUpperCase();
  const fullName = user?.username || user?.email || "Your account";

  return (
    <div className="mx-auto w-full max-w-7xl px-4 py-8 sm:px-6 lg:px-8 lg:py-12">
      <div className="mb-8">
        <p className="text-sm font-semibold uppercase tracking-[0.2em] text-red-600">
          Account
        </p>
        <h1 className="mt-2 text-3xl font-bold tracking-tight text-slate-900">
          Your profile
        </h1>
        <p className="mt-2 text-slate-500">
          Review the information connected to your account.
        </p>
        <div className="mt-5 flex flex-wrap gap-3">
          <Link
            to={path.updateProfile}
            className="rounded-xl bg-red-600 px-4 py-2.5 text-sm font-semibold text-white transition hover:bg-red-700"
          >
            Edit profile
          </Link>
          <Link
            to={path.changePassword}
            className="rounded-xl border border-slate-300 bg-white px-4 py-2.5 text-sm font-semibold text-slate-700 transition hover:bg-slate-50"
          >
            Change password
          </Link>
        </div>
      </div>
      <div className="grid gap-6 lg:grid-cols-[minmax(0,1fr)_20rem]">
        <section className="overflow-hidden rounded-3xl border border-slate-200 bg-white shadow-sm">
          <div className="h-28 bg-linear-to-r from-red-600 via-red-500 to-rose-500" />
          <div className="px-6 pb-7 sm:px-9">
            {user?.profile ? (
              <img
                src={user.profile}
                alt="Profile"
                className="-mt-12 h-24 w-24 rounded-3xl border-4 border-white object-cover shadow-sm"
              />
            ) : (
              <div className="-mt-12 grid h-24 w-24 place-items-center rounded-3xl border-4 border-white bg-red-100 text-2xl font-bold text-red-700 shadow-sm">
                {initials}
              </div>
            )}
            <h2 className="mt-5 text-2xl font-bold text-slate-900">
              {fullName || "Your account"}
            </h2>
            <p className="mt-1 text-slate-500">
              {user?.email || "No email available"}
            </p>
            <div className="mt-8 grid gap-5 border-t border-slate-100 pt-6 sm:grid-cols-2">
              <div>
                <p className="text-xs font-semibold uppercase tracking-wider text-slate-400">
                  Username
                </p>
                <p className="mt-2 font-medium text-slate-800">
                  {user?.username || "—"}
                </p>
              </div>
              <div>
                <p className="text-xs font-semibold uppercase tracking-wider text-slate-400">
                  Email address
                </p>
                <p className="mt-2 font-medium text-slate-800">
                  {user?.email || "—"}
                </p>
              </div>
              <div className="sm:col-span-2">
                <p className="text-xs font-semibold uppercase tracking-wider text-slate-400">
                  Phone number
                </p>
                <p className="mt-2 font-medium text-slate-800">
                  {user?.phone || "—"}
                </p>
              </div>
              <div className="sm:col-span-2">
                <p className="text-xs font-semibold uppercase tracking-wider text-slate-400">
                  Address
                </p>
                <p className="mt-2 font-medium text-slate-800">
                  {user?.address || "—"}
                </p>
              </div>
            </div>
          </div>
        </section>
        <aside className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm sm:p-7">
          <div
            className="grid h-11 w-11 place-items-center rounded-xl bg-emerald-100 text-emerald-700"
            aria-hidden="true"
          >
            ✓
          </div>
          <h2 className="mt-5 text-lg font-bold text-slate-900">
            Account protected
          </h2>
          <p className="mt-2 text-sm leading-6 text-slate-500">
            Your account is secured. Keep your sign-in details private.
          </p>
          <Link
            to={path.home}
            className="mt-6 inline-flex font-semibold text-red-600 transition hover:text-red-700"
          >
            Back to home{" "}
            <span className="ml-2" aria-hidden="true">
              →
            </span>
          </Link>
        </aside>
      </div>
    </div>
  );
};

export default Profile;
