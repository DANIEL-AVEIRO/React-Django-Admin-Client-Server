import { Link, useNavigate } from "react-router-dom";
import useAuth from "../../hooks/useAuth.js";
import path from "../../constants/path.js";

const Header = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate(path.login);
  };

  return (
    <header className="sticky top-0 z-20 border-b border-slate-200/80 bg-white/90 backdrop-blur-xl">
      <div className="mx-auto flex h-16 w-full max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
        <Link to={path.home} className="flex items-center gap-3 text-lg font-bold tracking-tight text-slate-900">
          <span className="grid h-9 w-9 place-items-center rounded-xl bg-red-600 text-sm text-white shadow-md shadow-red-600/20">D</span>
          Daniel
        </Link>
        <nav className="flex items-center gap-3 sm:gap-5">
          <Link to={path.home} className="hidden text-sm font-medium text-slate-600 transition hover:text-red-600 sm:block">Home</Link>
          <Link to={path.profile} className="text-sm font-medium text-slate-600 transition hover:text-red-600">Profile</Link>
          <span className="hidden h-8 w-px bg-slate-200 sm:block" />
          <span className="hidden max-w-36 truncate text-sm text-slate-500 md:block">{user?.first_name || user?.email || "Account"}</span>
          <button onClick={handleLogout} className="rounded-lg border border-slate-200 px-3 py-2 text-sm font-semibold text-slate-700 transition hover:border-rose-200 hover:bg-rose-50 hover:text-rose-700">Sign out</button>
        </nav>
      </div>
    </header>
  );
};

export default Header;
