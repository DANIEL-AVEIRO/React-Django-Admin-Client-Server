import { registerUser } from "../../api/services/auth";
import path from "../../constants/path";
import { useState } from "react";
import { toast } from "react-toastify";
import { Link, useNavigate } from "react-router-dom";
import { EyeIcon, EyeOff } from "lucide-react";
const Register = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [passwordToggle, setPasswordToggle] = useState(false);
  const [confirmPasswordToggle, setConfirmPasswordToggle] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    if (!username || !email || !password || !confirmPassword) {
      toast.error(
        "Username, email, password and confirm password are required",
      );
      setLoading(false);
      return;
    }
    if (password !== confirmPassword) {
      toast.error("Passwords do not match");
      setLoading(false);
      return;
    }

    try {
      const response = await registerUser({
        username: username,
        email,
        password,
      });
      toast.success(response.message);
      navigate(path.login);
    } catch (error) {
      toast.error(error.response.data.message);
    } finally {
      setLoading(false);
    }
  };
  return (
    <section className="w-full max-w-lg rounded-3xl border border-slate-200 bg-white p-7 shadow-xl shadow-slate-900/5 sm:p-10">
      <div className="mb-7">
        <p className="mb-2 text-sm font-semibold uppercase tracking-[0.2em] text-red-600">
          Get started
        </p>
        <h1 className="text-3xl font-bold tracking-tight text-slate-900">
          Create your account
        </h1>
        <p className="mt-2 text-sm leading-6 text-slate-500">
          A few details and you’ll be ready to go.
        </p>
      </div>
      <form className="space-y-4" onSubmit={handleSubmit}>
        <label className="block text-sm font-medium text-slate-700">
          Username
          <input
            type="text"
            placeholder="Username"
            autoComplete="given-name"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="mt-2 w-full rounded-xl border border-slate-300 px-4 py-3 outline-none transition placeholder:text-slate-400 focus:border-red-500 focus:ring-4 focus:ring-red-500/10"
          />
        </label>
        <label className="block text-sm font-medium text-slate-700">
          Email address
          <input
            type="email"
            placeholder="you@example.com"
            autoComplete="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="mt-2 w-full rounded-xl border border-slate-300 px-4 py-3 outline-none transition placeholder:text-slate-400 focus:border-red-500 focus:ring-4 focus:ring-red-500/10"
          />
        </label>
        <label className="block text-sm font-medium text-slate-700 relative">
          Password
          <input
            type={passwordToggle ? "text" : "password"}
            placeholder="Create a password"
            autoComplete="new-password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="mt-2 w-full rounded-xl border border-slate-300 px-4 py-3 outline-none transition placeholder:text-slate-400 focus:border-red-500 focus:ring-4 focus:ring-red-500/10"
          />
          <button
            type="button"
            onClick={() => setPasswordToggle(!passwordToggle)}
            className="absolute right-3 top-10 text-slate-500 cursor-pointer"
          >
            {passwordToggle ? (
              <EyeIcon className="h-4 w-4" />
            ) : (
              <EyeOff className="h-4 w-4" />
            )}
          </button>
        </label>
        <label className="block text-sm font-medium text-slate-700 relative">
          Confirm password
          <input
            type={confirmPasswordToggle ? "text" : "password"}
            placeholder="Enter your password again"
            autoComplete="new-password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            className="mt-2 w-full rounded-xl border border-slate-300 px-4 py-3 outline-none transition placeholder:text-slate-400 focus:border-red-500 focus:ring-4 focus:ring-red-500/10"
          />
          <button
            type="button"
            onClick={() => setConfirmPasswordToggle(!confirmPasswordToggle)}
            className="absolute right-3 top-10 text-slate-500 cursor-pointer"
          >
            {confirmPasswordToggle ? (
              <EyeIcon className="h-4 w-4" />
            ) : (
              <EyeOff className="h-4 w-4" />
            )}
          </button>
        </label>
        <button
          className="w-full rounded-xl bg-red-600 px-4 py-3 font-semibold text-white shadow-lg shadow-red-600/20 transition hover:bg-red-700 focus:outline-none focus:ring-4 focus:ring-red-500/20 disabled:cursor-not-allowed disabled:opacity-60"
          type="submit"
          disabled={loading}
        >
          {loading ? "Creating account…" : "Create account"}
        </button>
      </form>
      <p className="mt-6 text-center text-sm text-slate-500">
        Already have an account?{" "}
        <Link
          className="font-semibold text-red-600 hover:text-red-700"
          to={path.login}
        >
          Sign in
        </Link>
      </p>
    </section>
  );
};

export default Register;
