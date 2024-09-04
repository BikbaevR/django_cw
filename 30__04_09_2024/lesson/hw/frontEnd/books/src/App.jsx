
import './App.css'
import GetBooks from './books/GetBooks.jsx'
import AddBook from './books/AddBook.jsx'

function App() {
  const domainName = 'http://127.0.0.1:8000/api/books/v1/'

  return (
    <div>
        <GetBooks domainName={domainName} />
        <AddBook domainName={domainName} />
    </div>
  )
}

export default App
