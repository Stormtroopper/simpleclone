import type{ComponentProps} from 'react'
type ButtonProps=ComponentProps<"button">&{
    error?:string,
    variant?:'primary'|'secondary'
}
const variants={
    primary:'bg-red-600 hover:bg-red-700',
    secondary:'bg-gray-800 hover:bg-gray-900'
}
export const Button=({error,variant='primary',className="",...props}:ButtonProps)=>{
    const btnid=props.name
    return (
    <>
      <div>
        <button
          id={btnid}
          className={`rounded-md px-4 py-2 text-sm font-medium text-white disabled:cursor-not-allowed disabled:opacity-50 ${variants[variant]} ${className}`}
          {...props}
        />
        {error && <p className="mt-1 text-xs text-red-600">{error}</p>}
      </div>
    </>
  );
}