import { Outlet } from "react-router-dom";

const AuthLayout = () => {
  return (
    <main className="relative flex min-h-screen items-center justify-center overflow-hidden bg-slate-100 px-4 py-10 sm:px-6">
      <div className="absolute -left-24 -top-24 h-72 w-72 rounded-full bg-red-200/60 blur-3xl" />
      <div className="absolute -bottom-28 -right-16 h-80 w-80 rounded-full bg-rose-200/60 blur-3xl" />
      <div className="relative grid w-full max-w-5xl overflow-hidden rounded-[2rem] bg-white shadow-2xl shadow-slate-900/10 lg:grid-cols-[0.9fr_1.1fr]">
        <aside className="hidden flex-col justify-between bg-red-700 p-12 text-white lg:flex">
          <div className="flex items-center gap-3 text-lg font-bold"><span className="grid h-10 w-10 place-items-center rounded-xl bg-white/15">D</span> Daniel</div>
          <div>
            <p className="mb-5 text-sm font-semibold uppercase tracking-[0.25em] text-red-200">A better way to begin</p>
            <h2 className="text-4xl font-bold leading-tight">Make space for what matters.</h2>
            <p className="mt-5 max-w-sm leading-7 text-red-100">A clear, calm place to manage your account and keep moving forward.</p>
          </div>
          <p className="text-sm text-red-200">Simple by design. Ready when you are.</p>
        </aside>
        <section className="flex items-center justify-center p-5 sm:p-10 lg:p-12">
          <Outlet />
        </section>
      </div>
    </main>
  );
};

export default AuthLayout;
