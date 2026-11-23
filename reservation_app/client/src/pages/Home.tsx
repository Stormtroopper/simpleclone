interface HomeProps{
  isAuthenticated:boolean
}
const Home = ({isAuthenticated}:HomeProps) => {

  return (
    <div>
      <h1 className="text-4xl font-bold text-red-600">
        Welcome to the Home Page!
      </h1>

    </div>
  )
}

export default Home
