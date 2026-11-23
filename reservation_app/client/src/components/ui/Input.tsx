import type { ComponentProps } from "react";
type InputProps = ComponentProps<"input"> & {
  label: string;
  error?: string;
};
export const Input = ({
  label,
  error,
  id,
  className = "",
  ...props
}: InputProps) => {
  const inputId = id ?? props.name;
  return (
    <>
      <div>
        <label
          htmlFor={inputId}
          className="mb-1 block text-sm font-medium text-gray-700"
        >
          {label}
        </label>
        <input
          id={inputId}
          aria-invalid={error ? true : undefined}
          className={`w-full rounded-md border px-3 py-2 text-sm focus:outline-none ${
            error ? "border-red-500" : "border-gray-300 focus:border-red-500"
          } ${className}`}
          {...props}
        />
        {error && <p className="mt-1 text-xs text-red-600">{error}</p>}
      </div>
    </>
  );
};
