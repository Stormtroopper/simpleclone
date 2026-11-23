import type { ReactNode } from 'react'
import {Navigate,useLocation} from 'react-router-dom'

interface ProtectedRouteProps {
    children: ReactNode
    isAuthenticated: boolean
}
export const ProtectedRoute=({children,isAuthenticated}:ProtectedRouteProps)=>{
const location=useLocation()
if(isAuthenticated){
    return <>{children}</>
}
return <Navigate to="/login" state={{from:location.pathname}} replace />
}