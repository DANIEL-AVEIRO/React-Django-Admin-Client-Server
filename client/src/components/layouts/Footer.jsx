const Footer = () => (
  <footer className="border-t border-slate-200 bg-white">
    <div className="mx-auto flex w-full max-w-7xl flex-col gap-2 px-4 py-5 text-sm text-slate-500 sm:flex-row sm:items-center sm:justify-between sm:px-6 lg:px-8">
      <p>© {new Date().getFullYear()} Daniel. All rights reserved.</p>
      <p>Made for a little more clarity.</p>
    </div>
  </footer>
);

export default Footer;
