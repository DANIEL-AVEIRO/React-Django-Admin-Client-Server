import { Outlet } from "react-router-dom";

const BlankLayout = () => {
  return (
    <div className="min-h-screen bg-slate-50">
      <Outlet />
    </div>
  );
};

export default BlankLayout;
