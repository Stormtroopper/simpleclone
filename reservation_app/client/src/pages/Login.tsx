import { useDispatch } from "react-redux";
import type { AppDispatch } from "../store/store";
import { Link, Navigate, useLocation } from "react-router-dom";
import { useForm, type SubmitHandler } from "react-hook-form";
import { api } from "../utils/api";
import { loginFailure, loginSuccess } from "../reducers/slices/authSlice";
import { Input } from "../components/ui/Input";
import { Button } from "../components/ui/Button";

interface LoginResponse {
  user: { id: string; name: string; email: string };
  token: string;
}
interface LoginFormValues {
  email: string;
  password: string;
}

interface LoginProps {
  isAuthenticated: boolean;
}
export const Login = ({ isAuthenticated }: LoginProps) => {
  const dispatch = useDispatch<AppDispatch>();
  const location = useLocation();
  const from =
    (location.state as { from?: string } | null)?.from ?? "/restaurants";
  const {
    register,
    handleSubmit,
    setError,
    formState: { errors, isSubmitting },
  } = useForm<LoginFormValues>({ defaultValues: { email: "", password: "" } });
  if (isAuthenticated) {
    return <Navigate to={from} replace />;
  }
  const onSubmit: SubmitHandler<LoginFormValues> = async (values) => {
    try {
      // NOTE: the server does not expose /auth/login yet.
      const data = await api<LoginResponse>("/auth/login", {
        method: "POST",
        body: JSON.stringify(values),
      });
      dispatch(loginSuccess(data));
    } catch (err) {
      dispatch(loginFailure());
      setError("root.server", {
        message: err instanceof Error ? err.message : "Login failed",
      });
    }
  };
  return (
    <>
      <div className="mx-auto max-w-sm px-4 py-12">
        <h1 className="mb-6 text-2xl font-bold text-gray-800">Log in</h1>
        <form
          onSubmit={handleSubmit(onSubmit)}
          noValidate
          className="space-y-4 rounded-lg bg-white p-6 shadow"
        >
          <Input
            label="Email"
            type="email"
            autoComplete="email"
            error={errors.email?.message}
            {...register("email", {
              required: "Email is required",
              pattern: {
                value: /^\S+@\S+\.\S+$/,
                message: "Enter a valid email address",
              },
            })}
          />
          <Input
            label="Password"
            type="password"
            autoComplete="current-password"
            error={errors.password?.message}
            {...register("password", { required: "Password is required" })}
          />
          {errors.root?.server && (
            <p className="text-sm text-red-600">{errors.root.server.message}</p>
          )}
          <Button type="submit" disabled={isSubmitting} className="w-full">
            {isSubmitting ? "Logging in..." : "Log in"}
          </Button>
        </form>
        <p className="mt-4 text-center text-sm text-gray-600">
        No account?{' '}
        <Link to="/register" className="text-red-600 hover:underline">
          Register
        </Link>
      </p>
      </div>
    </>
  );
};
