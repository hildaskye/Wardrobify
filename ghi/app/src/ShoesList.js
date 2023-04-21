import { useState, useEffect } from 'react';

function ShoesList() {

    const [shoes, setShoes] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const url = "http://localhost:8080/api/shoes/";
            const response = await fetch(url);
            console.log(response)
            if (response.ok) {
                const data = await response.json();
                setShoes(data.shoes);
            }
        }
        fetchData();
    }, []);


    const deleteShoe = async (id) => {

        const deleteFunctionUrl = `http://localhost:8080/api/shoes/${id}/`
        const options = {
            method: 'DELETE',
            headers: {
                "Content-Type": "application/json"
            }

        }
        const response = await fetch(deleteFunctionUrl, options)
        if (response.ok) {
            setShoes(shoes.filter(shoe => shoe.id !== id));
        }
    }


    return (
        <table className="table table-striped">
        <thead>
          <tr>
            <th>Manufacturer</th>
            <th>Model Name</th>
            <th>Color</th>
            <th>Picture</th>
            <th>Closet</th>
            <th>Delete</th>
          </tr>
        </thead>
        <tbody>
        {shoes.map(shoe => {
          return (
            <tr key={shoe.id}>
              <td>{ shoe.manufacturer } </td>
              <td>{ shoe.model_name }</td>
              <td>{ shoe.color }</td>
              <td><img src={shoe.picture_url} alt="unavailable" width="100" height="100" /></td>
              <td>{ shoe.shoe_bin.closet_name }</td>
              <td>
                <button type="button" className="btn btn-danger"
                onClick={() => deleteShoe(shoe.id)}
                >Delete</button>
              </td>
            </tr>
          );
        })}
        </tbody>
      </table>
    );
}

export default ShoesList;
