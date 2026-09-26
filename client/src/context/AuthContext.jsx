import { useState } from "react";
import { createContext } from "react";

export const AuthContext = createContext(null);

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
    const savedToken = localStorage.getItem("token");
    if (!savedToken) return null;
    try {
      return JSON.parse(savedToken) || null;
    } catch {
      return savedToken;
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

  const updateUser = (data) => {
    setUser({ ...user, ...data });
    localStorage.setItem("user", JSON.stringify({ ...user, ...data }));
  };

  return (
    <AuthContext.Provider value={{ user, token, login, logout, updateUser }}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthProvider;
