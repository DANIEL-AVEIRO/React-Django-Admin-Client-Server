import api from "../axios";
import endpoints from "../endpoints";

export const login = async (data) => {
  const response = await api.post(endpoints.login, data);
  return response.data;
};

export const register = async (data) => {
  const response = await api.post(endpoints.register, data);
  return response.data;
};

export const profile = async () => {
  const response = await api.get(endpoints.profile);
  return response.data;
};

export const updateProfile = async (data) => {
  const response = await api.put(endpoints.updateProfile, data);
  return response.data;
};

export const changePassword = async (data) => {
  const response = await api.put(endpoints.changePassword, data);
  return response.data;
};

export const logout = async () => {
  const response = await api.post(endpoints.logout);
  return response.data;
};
