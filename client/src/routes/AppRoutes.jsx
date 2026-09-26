import { BrowserRouter, Routes, Route } from "react-router-dom";
import MainLayout from "../layouts/MainLayout";
import AuthLayout from "../layouts/AuthLayout";
import Home from "../pages/home/Home";
import Profile from "../pages/profile/Profile";
import UpdateProfile from "../pages/profile/UpdateProfile";
import ChangePassword from "../pages/profile/ChangePassword";
import Login from "../pages/auth/Login";
import Register from "../pages/auth/Register";
import ProtectedRoute from "./ProtectedRoutes";
import path from "../constants/path";
import { ToastContainer } from "react-toastify";

const AppRoutes = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path={path.home} element={<MainLayout />}>
          <Route index element={<Home />} />

          <Route element={<ProtectedRoute />}>
            <Route path={path.profile} element={<Profile />} />
            <Route path={path.updateProfile} element={<UpdateProfile />} />
            <Route path={path.changePassword} element={<ChangePassword />} />
          </Route>
        </Route>

        <Route element={<AuthLayout />}>
          <Route path={path.login} element={<Login />} />
          <Route path={path.register} element={<Register />} />
        </Route>
      </Routes>
      <ToastContainer />
    </BrowserRouter>
  );
};

export default AppRoutes;
