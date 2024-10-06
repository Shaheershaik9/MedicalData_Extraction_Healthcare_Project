import {useState} from 'react'
function Prescription()
{
const [file,sendFile]=useState({
file_format:'prescription',
file:''

})
console.log('file',file)
//  console.log('file uploaded',file)
const handleSubmit=(event)=>
{
    const inputFile=event.target.value;
    sendFile({...file,file:inputFile})
}

const ApiCall=()=>
{
fetch('http://127.0.0.1:8000/extract_from_doc', {
    mode:'no-cors',
    method: 'POST',
    body: file
  })
  .then(response => response.json())
  .then(data => {
    console.log('success',data)
  })
  .catch(error => {
    console.error('fail',error)
  })

}

return(
<div className='container'>

<div className='row  mt-5'>
<div className='col-12 mt-2 '>
 <label className='text text-info'>Please upload file</label>
</div>
<div className='col-12 mt-2'>
<input type='file' onChange={(event)=>handleSubmit(event)}></input>
</div>
<div className='col-12 mt-4'>
<button className='btn btn-success' onClick={()=>ApiCall()}>Submit</button>
</div>

</div>






</div>
)
}

export default Prescription