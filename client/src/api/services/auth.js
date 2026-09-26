import api from "../axios";
import endpoints from "../endpoints";

export const loginUser = async (data) => {
  const response = await api.post(endpoints.auth.login, data);
  return response.data;
};

export const registerUser = async (data) => {
  const response = await api.post(endpoints.auth.register, data);
  return response.data;
};

export const profile = async () => {
  const response = await api.get(endpoints.auth.profile);
  return response.data;
};

export const updateProfile = async (data) => {
  const response = await api.put(endpoints.auth.updateProfile, data);
  return response.data;
};

export const changePassword = async (data) => {
  const response = await api.put(endpoints.auth.changePassword, data);
  return response.data;
};

export const logoutUser = async () => {
  const response = await api.post(endpoints.auth.logout);
  return response.data;
};
