import { logout } from "../../reducers/slices/authSlice";
import { useDispatch } from "react-redux";
import { useEffect } from "react";
import { broadcastLogout, listenToLogout } from "../../utils/broadcast";
import { NavLink } from "react-router-dom";

const linkClass = ({ isActive }: { isActive: boolean }) =>
  isActive
    ? "rounded px-3 py-2 text-red-600"
    : "rounded px-3 py-2 text-gray-700 hover:text-red-600";
interface NavBarProps {
  isAuthenticated: boolean;
}
export const NavBar = (isAuthenticated: NavBarProps) => {
  const dispatch = useDispatch();
  useEffect(() => {
    // Listen to other Tabs logout event and dispatch logout action
    listenToLogout(() => {
      dispatch(logout());
      // redirect to login page after logout
      window.location.href = "/login";
    });
  }, []);
  const handleLogout = () => {
    dispatch(logout());
    // Notify all the tabs about the logout event

    broadcastLogout();
    window.location.href = "/login";
  };
  return (
    <>
      <nav className="bg-white shadow">
        <div className="mx-auto flex max-w-5xl items-center gap-2 px-4 py-3">
          <span className="mr-4 text-lg font-bold text-red-600">
            Reservations
          </span>
          <NavLink to="/" end className={linkClass}>
            Home
          </NavLink>
          {isAuthenticated ? (
            <>
              <NavLink to="/bookings" className={linkClass}>
                My Bookings
              </NavLink>
              <NavLink to="/restaurants" className={linkClass}>
                Restaurants
              </NavLink>
            </>
          ) : (
            <>
              <div className="ml-auto flex gap-2">
                <NavLink to="/login" className={linkClass}>
                  Log in
                </NavLink>
                <NavLink to="/register" className={linkClass}>
                  Register
                </NavLink>
              </div>
            </>
          )}
        </div>
      </nav>
      <button onClick={handleLogout}>Logout</button>
    </>
  );
};
