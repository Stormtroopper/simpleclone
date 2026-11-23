import { Link, Navigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { loginSuccess } from "../reducers/slices/authSlice";
import type { AppDispatch } from "../store/store";
import { useForm, type SubmitHandler } from "react-hook-form";
import { Input } from "../components/ui/Input";
import { Button } from "../components/ui/Button";
import { api } from "../utils/api";

interface CreatedUserProps {
  id?: string;
  _id?: string;
  name: string;
  email?: string;
}
interface RegisterProps {
  isAuthenticated: boolean;
}
interface RegisterFormValues {
  name: string;
  email: string;
  phoneNo: number;
  password: string;
  confirmPassword: string;
}
export const Register = ({ isAuthenticated }: RegisterProps) => {
  const dispatch = useDispatch<AppDispatch>();
  if (isAuthenticated) {
    return <Navigate to="/" replace />;
  }
  const {
    register,
    setError,
    getValues,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<RegisterFormValues>({
    defaultValues: {
      name: "",
      email: "",
      phoneNo: 0,
      password: "",
      confirmPassword: "",
    },
  });
  //       const [form, setForm] = useState({
  //     firstName: '',
  //     lastName: '',
  //     email: '',
  //     phone: '',
  //     password: '',
  //   })
  const onSubmit: SubmitHandler<RegisterFormValues> = async (values) => {
    try {
      const created = await api<CreatedUserProps>("/users", {
        method: "POST",
        body: JSON.stringify({
          name: values?.name,
          email: values?.email,
          phone: values?.phoneNo || null,
          password: values?.password,
        }),
      });
      const id = created.id ?? created?._id ?? "";
      dispatch(
        loginSuccess({
          user: {
            id,
            name: `${created.name}`,
            email: `${created.email}`,
          },
          token: id,
        }),
      );
    } catch (err) {
        setError('root.server', {
        message: err instanceof Error ? err.message : 'Registration failed',
      })
    }
  };
  return(
    <>
    <div className="mx-auto max-w-sm px-4 py-12">
      <h1 className="mb-6 text-2xl font-bold text-gray-800">Create an account</h1>
      <form
        onSubmit={handleSubmit(onSubmit)}
        noValidate
        className="space-y-4 rounded-lg bg-white p-6 shadow"
      >
  
        <Input
          label="Last name"
          autoComplete="family-name"
          error={errors.name?.message}
          {...register('name', { required: 'Last name is required' })}
        />
        <Input
          label="Email"
          type="email"
          autoComplete="email"
          error={errors.email?.message}
          {...register('email', {
            required: 'Email is required',
            pattern: { value: /^\S+@\S+\.\S+$/, message: 'Enter a valid email address' },
          })}
        />
        <Input
          label="Phone (optional)"
          type="tel"
          autoComplete="tel"
          error={errors.phoneNo?.message}
          {...register('phoneNo', {
            pattern: { value: /^[+\d][\d\s-]{6,}$/, message: 'Enter a valid phone number' },
          })}
        />
        <Input
          label="Password"
          type="password"
          autoComplete="new-password"
          error={errors.password?.message}
          {...register('password', {
            required: 'Password is required',
            minLength: { value: 6, message: 'Password must be at least 6 characters' },
          })}
        />
        <Input
          label="Confirm password"
          type="password"
          autoComplete="new-password"
          error={errors.confirmPassword?.message}
          {...register('confirmPassword', {
            required: 'Please confirm your password',
            validate: (value) => value === getValues('password') || 'Passwords do not match',
          })}
        />
        {errors.root?.server && (
          <p className="text-sm text-red-600">{errors.root.server.message}</p>
        )}
        <Button type="submit" disabled={isSubmitting} className="w-full">
          {isSubmitting ? 'Creating account...' : 'Register'}
        </Button>
      </form>
      <p className="mt-4 text-center text-sm text-gray-600">
        Already registered?{' '}
        <Link to="/login" className="text-red-600 hover:underline">
          Log in
        </Link>
      </p>
    </div>
    </>
  )
};
