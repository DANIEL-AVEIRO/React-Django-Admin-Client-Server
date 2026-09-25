import { Navigate, Outlet } from "react-router-dom";
import useAuth from "../hooks/useAuth.js";
import path from "../constants/path.js";

const ProtectedRoute = () => {
  const { token } = useAuth();
  return token ? <Outlet /> : <Navigate to={path.login} />;
};

export default ProtectedRoute;
