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

    return (
        <table className="table table-striped">
        <thead>
          <tr>
            <th>Manufacturer</th>
            <th>Model Name</th>
            <th>Color</th>
            <th>Picture</th>
            <th>Closet</th>
          </tr>
        </thead>
        <tbody>
        {shoes.map(shoe => {
          return (
            <tr key={shoe.id}>
              <td>{ shoe.manufacturer } </td>
              <td>{ shoe.model_name }</td>
              <td>{ shoe.color }</td>
              <img src={shoe.picture_url} alt="unavailable" width="100" height="100" />
              <td>{ shoe.shoe_bin.closet_name }</td>
            </tr>
          );
        })}
        </tbody>
      </table>
    );
}

export default ShoesList;
