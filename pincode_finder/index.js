fetchData()



async function fetchData(){
    try{

        const PinCode = document.getElementById("PinCode").value
        const response = await fetch(`http://127.0.0.1:8000/pincode/${PinCode}`)
        if (!response.ok){
            throw new Error("could not fetch resource");
        }
        const data = await response.json();
        console.log(data);

    }
    catch(error){console.log(error)}
}