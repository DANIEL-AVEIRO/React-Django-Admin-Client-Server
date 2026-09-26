import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import { changePassword } from "../../api/services/auth.js";
import path from "../../constants/path.js";
import useAuth from "../../hooks/useAuth.js";

const ChangePassword = () => {
  const { logout } = useAuth();
  const navigate = useNavigate();
  const [currentPassword, setCurrentPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    if (!currentPassword || !newPassword || !confirmPassword) {
      toast.error("All fields are required");
      setLoading(false);
      return;
    }
    if (newPassword !== confirmPassword) {
      toast.error("New passwords do not match.");
      setLoading(false);
      return;
    }

    try {
      const response = await changePassword({
        current_password: currentPassword,
        new_password: newPassword,
      });
      logout();
      toast.success(response.message);
      navigate(path.login, { replace: true });
    } catch (error) {
      toast.error(error.response.data.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mx-auto w-full max-w-3xl px-4 py-8 sm:px-6 lg:px-8 lg:py-12">
      <Link
        to={path.profile}
        className="text-sm font-semibold text-red-600 hover:text-red-700"
      >
        ← Back to profile
      </Link>
      <div className="mt-5 rounded-3xl border border-slate-200 bg-white p-6 shadow-sm sm:p-9">
        <p className="text-sm font-semibold uppercase tracking-[0.2em] text-red-600">
          Security
        </p>
        <h1 className="mt-2 text-3xl font-bold tracking-tight text-slate-900">
          Change password
        </h1>
        <p className="mt-2 text-slate-500">
          Choose a new password for your account.
        </p>
        <form onSubmit={handleSubmit} className="mt-8 space-y-5">
          <label className="block text-sm font-medium text-slate-700">
            Current password
            <input
              className="mt-2 w-full rounded-xl border border-slate-300 bg-white px-4 py-3 text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-red-500 focus:ring-4 focus:ring-red-500/10"
              name="current_password"
              type="password"
              value={currentPassword}
              onChange={(e) => setCurrentPassword(e.target.value)}
              autoComplete="current-password"
            />
          </label>
          <label className="block text-sm font-medium text-slate-700">
            New password
            <input
              className="mt-2 w-full rounded-xl border border-slate-300 bg-white px-4 py-3 text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-red-500 focus:ring-4 focus:ring-red-500/10"
              name="new_password"
              type="password"
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
              autoComplete="new-password"
            />
          </label>
          <label className="block text-sm font-medium text-slate-700">
            Confirm new password
            <input
              className="mt-2 w-full rounded-xl border border-slate-300 bg-white px-4 py-3 text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-red-500 focus:ring-4 focus:ring-red-500/10"
              name="confirm_password"
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              autoComplete="new-password"
            />
          </label>
          <div className="rounded-xl bg-amber-50 p-4 text-sm leading-6 text-amber-800">
            You’ll be signed out after changing your password. Sign in again
            with your new password.
          </div>
          <div className="flex flex-col-reverse gap-3 pt-2 sm:flex-row sm:justify-end">
            <Link
              to={path.profile}
              className="rounded-xl border border-slate-300 px-5 py-3 text-center text-sm font-semibold text-slate-700 hover:bg-slate-50"
            >
              Cancel
            </Link>
            <button
              disabled={loading}
              type="submit"
              className="rounded-xl bg-red-600 px-5 py-3 text-sm font-semibold text-white transition hover:bg-red-700 disabled:cursor-not-allowed disabled:opacity-60"
            >
              {loading ? "Updating…" : "Update password"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default ChangePassword;
