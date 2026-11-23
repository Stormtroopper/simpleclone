import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import Home from './pages/Home'
import { Login } from './pages/Login'
import { useSelector } from 'react-redux'
import type { RootState } from './store/store'
import { ProtectedRoute } from './components/ui/ProtectedRoute'
import RestaurantCard from './components/restaurants/RestaurantCard'
import { RestaurantList } from './components/restaurants/RestaurantList'
function App() {
  const isAuthenticated=useSelector((state:RootState)=>state.auth.isAuthenticated)
  return (
    <>
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <h1 className="text-4xl font-bold text-red-600">
        Tailwind is working!
      </h1>
    </div>
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login isAuthenticated={isAuthenticated} />} />
        <Route path="/restaurants"element={<ProtectedRoute isAuthenticated={isAuthenticated} >
          <RestaurantCard/>
        </ProtectedRoute>} />
                <Route path="/restaurants"element={<ProtectedRoute isAuthenticated={isAuthenticated} >
          <RestaurantList/>
        </ProtectedRoute>} />
      </Routes>
    </Router>
    </>
  )
}

export default App