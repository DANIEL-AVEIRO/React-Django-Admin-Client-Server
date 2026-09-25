import { useState } from "react";
import { AuthContext } from "./AuthContextInstance.js";

const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(() => {
    try {
      return JSON.parse(localStorage.getItem("user")) || null;
    } catch {
      localStorage.removeItem("user");
      return null;
    }
  });

  const [token, setToken] = useState(() => {
    try {
      return JSON.parse(localStorage.getItem("token")) || null;
    } catch {
      localStorage.removeItem("token");
      return null;
    }
  });

  const login = (response) => {
    const userData = response.data;

    setUser(userData);
    setToken(userData.token);

    localStorage.setItem("user", JSON.stringify(userData));
    localStorage.setItem("token", userData.token);
  };

  const logout = () => {
    setUser(null);
    setToken(null);

    localStorage.removeItem("user");
    localStorage.removeItem("token");
  };

  return (
    <AuthContext.Provider value={{ user, token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthProvider;
