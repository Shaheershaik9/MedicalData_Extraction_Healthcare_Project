import {Link} from 'react-router-dom'
function HomePage() {

        return(
        <div className='container'>
        <div className='row'>
        <div className='col-12'>
                <h1 className='text  text-center mt-3 border' style={{backgroundColor:'yellow',color:'black'}}> Medical Data Extractor</h1>
        </div>

        </div>
        <div className=' row mt-5'>
        <div className='col-9'>

           </div>
            <div className='col-3'>
               <Link to='/prescription'> <button className='btn btn-success mr-3'>Prescription</button></Link>
                <button className='btn btn-success'>Patient Details</button>

            </div>
        </div>
        </div>
  )
}

export default HomePage;
