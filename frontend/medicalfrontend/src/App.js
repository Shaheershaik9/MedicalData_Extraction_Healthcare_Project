import {BrowserRouter,Route,Routes} from 'react-router-dom'
import HomePage from './homePage.js'
import Prescription from './prescriptionPage.js'
function App() {

        return(
        <BrowserRouter>
        <Routes>
            <Route path='/' element={<HomePage></HomePage>}></Route>
            <Route path='/prescription' element={<Prescription></Prescription>}></Route>
        </Routes>
        </BrowserRouter>
  )
}

export default App;
