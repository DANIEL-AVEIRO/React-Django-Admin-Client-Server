import { Link, useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import { updateProfile } from "../../api/services/auth.js";
import path from "../../constants/path.js";
import { useState } from "react";
import useAuth from "../../hooks/useAuth";

const UpdateProfile = () => {
  const { user, updateUser } = useAuth();
  const [username, setUsername] = useState(() => user?.username || "");
  const [email, setEmail] = useState(() => user?.email || "");
  const [phone, setPhone] = useState(() => user?.phone || "");
  const [address, setAddress] = useState(() => user?.address || "");
  const [profileImage, setProfileImage] = useState(null);
  const [preview, setPreview] = useState(() => user?.profile || "");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    if (!username || !email) {
      toast.error("Username and email are required");
      setLoading(false);
      return;
    }
    try {
      const formData = new FormData();
      formData.append("username", username);
      formData.append("email", email);
      formData.append("phone", phone);
      formData.append("address", address);
      if (profileImage) formData.append("profile", profileImage);

      const response = await updateProfile(formData);
      updateUser(response.data);
      toast.success(response.message);
      navigate(path.profile);
    } catch (error) {
      toast.error(error.response.data.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mx-auto w-full max-w-3xl px-4 py-8 sm:px-6 lg:px-8 lg:py-12">
      <Link
        to={path.profile}
        className="text-sm font-semibold text-red-600 hover:text-red-700"
      >
        ← Back to profile
      </Link>
      <div className="mt-5 rounded-3xl border border-slate-200 bg-white p-6 shadow-sm sm:p-9">
        <p className="text-sm font-semibold uppercase tracking-[0.2em] text-red-600">
          Profile settings
        </p>
        <h1 className="mt-2 text-3xl font-bold tracking-tight text-slate-900">
          Update your details
        </h1>
        <p className="mt-2 text-slate-500">
          Edit the contact information on your account.
        </p>
        <form onSubmit={handleSubmit} className="mt-8 space-y-5">
          <div className="flex flex-col gap-5 rounded-2xl bg-slate-50 p-5 sm:flex-row sm:items-center">
            {preview ? (
              <img
                src={preview}
                alt="Profile preview"
                className="h-24 w-24 rounded-2xl border border-slate-200 object-cover"
              />
            ) : (
              <div className="grid h-24 w-24 place-items-center rounded-2xl bg-red-100 text-2xl font-bold text-red-700">
                {username?.[0]?.toUpperCase() || "U"}
              </div>
            )}
            <div>
              <label
                className="block text-sm font-semibold text-slate-800"
                htmlFor="profile-image"
              >
                Profile photo
              </label>
              <p className="mt-1 text-sm text-slate-500">
                Choose an image file (JPG, PNG or WebP).
              </p>
              <input
                id="profile-image"
                type="file"
                accept="image/jpeg,image/png,image/webp"
                onChange={(event) => {
                  if (preview.startsWith("blob:")) URL.revokeObjectURL(preview);
                  const file = event.target.files?.[0] || null;
                  setProfileImage(file);
                  setPreview(
                    file ? URL.createObjectURL(file) : user?.profile || "",
                  );
                }}
                className="mt-3 block w-full text-sm text-slate-600 file:mr-4 file:rounded-lg file:border-0 file:bg-red-100 file:px-4 file:py-2 file:font-semibold file:text-red-700 hover:file:bg-red-200"
              />
            </div>
          </div>
          <label className="block text-sm font-medium text-slate-700">
            Username
            <input
              className="mt-2 w-full rounded-xl border border-slate-300 bg-white px-4 py-3 text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-red-500 focus:ring-4 focus:ring-red-500/10"
              autoComplete="username"
              required
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </label>
          <label className="block text-sm font-medium text-slate-700">
            Email address
            <input
              className="mt-2 w-full rounded-xl border border-slate-300 bg-white px-4 py-3 text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-red-500 focus:ring-4 focus:ring-red-500/10"
              type="email"
              autoComplete="email"
              required
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </label>
          <label className="block text-sm font-medium text-slate-700">
            Phone number
            <input
              className="mt-2 w-full rounded-xl border border-slate-300 bg-white px-4 py-3 text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-red-500 focus:ring-4 focus:ring-red-500/10"
              type="tel"
              autoComplete="tel"
              value={phone}
              onChange={(e) => setPhone(e.target.value)}
            />
          </label>
          <label className="block text-sm font-medium text-slate-700">
            Address
            <textarea
              className="mt-2 w-full rounded-xl border border-slate-300 bg-white px-4 py-3 text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-red-500 focus:ring-4 focus:ring-red-500/10 min-h-28 resize-y"
              autoComplete="street-address"
              value={address}
              onChange={(e) => setAddress(e.target.value)}
            />
          </label>
          <div className="flex flex-col-reverse gap-3 pt-2 sm:flex-row sm:justify-end">
            <Link
              to={path.profile}
              className="rounded-xl border border-slate-300 px-5 py-3 text-center text-sm font-semibold text-slate-700 hover:bg-slate-50"
            >
              Cancel
            </Link>
            <button
              type="submit"
              className="rounded-xl bg-red-600 px-5 py-3 text-sm font-semibold text-white transition hover:bg-red-700 disabled:cursor-not-allowed disabled:opacity-60"
              disabled={loading}
            >
              {loading ? "Saving..." : "Save changes"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default UpdateProfile;
