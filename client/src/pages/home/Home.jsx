import { Link } from "react-router-dom";
import useAuth from "../../hooks/useAuth.js";
import path from "../../constants/path.js";

const Home = () => {
  const { user } = useAuth();
  const firstName = user?.first_name || user?.firstName || "there";

  return (
    <div className="mx-auto w-full max-w-7xl px-4 py-8 sm:px-6 lg:px-8 lg:py-12">
      <section className="relative overflow-hidden rounded-[2rem] bg-red-700 px-7 py-10 text-white shadow-xl shadow-red-900/10 sm:px-12 sm:py-14">
        <div className="absolute -right-16 -top-24 h-72 w-72 rounded-full border-[40px] border-white/10" />
        <div className="absolute -bottom-36 right-44 h-64 w-64 rounded-full bg-rose-400/20 blur-2xl" />
        <div className="relative max-w-2xl">
          <p className="mb-4 text-sm font-semibold uppercase tracking-[0.22em] text-red-200">Your space, your pace</p>
          <h1 className="text-4xl font-bold tracking-tight sm:text-5xl">Good to see you, {firstName}.</h1>
          <p className="mt-5 max-w-xl text-base leading-7 text-red-100 sm:text-lg">Welcome to your personal dashboard. Your account details are ready whenever you need them.</p>
          <Link to={path.profile} className="mt-8 inline-flex items-center rounded-xl bg-white px-5 py-3 font-semibold text-red-700 shadow-lg transition hover:bg-red-50">View your profile <span className="ml-2" aria-hidden="true">→</span></Link>
        </div>
      </section>
      <section className="mt-8 grid gap-5 md:grid-cols-3">
        <article className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm md:col-span-2">
          <p className="text-sm font-semibold text-red-600">A good place to start</p>
          <h2 className="mt-2 text-xl font-bold text-slate-900">Your account is all yours.</h2>
          <p className="mt-2 max-w-xl leading-6 text-slate-500">Keep your profile information up to date and make changes to your account securely.</p>
        </article>
        <article className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
          <div className="grid h-11 w-11 place-items-center rounded-xl bg-rose-100 text-xl text-rose-700" aria-hidden="true">✦</div>
          <h2 className="mt-4 font-bold text-slate-900">Need a hand?</h2>
          <p className="mt-1 text-sm leading-6 text-slate-500">Your profile is the place to manage your account details.</p>
        </article>
      </section>
    </div>
  );
};

export default Home;
