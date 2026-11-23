import type{ComponentProps} from 'react'
type ButtonProps=ComponentProps<"button">&{
    error?:string
}
export const Button=({error,id,className="",...props}:ButtonProps)=>{
    const btnid=id??props.name
    return (
    <>
      <div>
       
        <button
          id={btnid}
          className={`rounded-md bg-red-600 px-4 py-2 text-sm font-medium text-white hover:bg-red-700 disabled:cursor-not-allowed disabled:opacity-50 ${className}`}
          {...props}
        />
        {error && <p className="mt-1 text-xs text-red-600">{error}</p>}
      </div>
    </>
  );
}