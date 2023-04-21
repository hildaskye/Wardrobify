import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function HatsList() {

    const [hats, setHats] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const url = "http://localhost:8090/api/hats/";
            const response = await fetch(url);
            if (response.ok) {
                const data = await response.json();
                setHats(data.hats);
            }
        }
        fetchData();
    }, []);

    const deleteHat = async (id) => {

        const deleteFunctionUrl = `http://localhost:8090/api/hats/${id}/`
        const options = {
            method: 'DELETE',
            headers: {
                "Content-Type": "application/json"
            }

        }
        const response = await fetch(deleteFunctionUrl, options)
        if (response.ok) {
            setHats(hats.filter(hat => hat.id !== id));
        }
    }


    return (
      <>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Picture</th>
            <th>Style Name</th>
            <th>Fabric</th>
            <th>Color</th>
            <th>Location</th>
          </tr>
        </thead>
        <tbody>
        {hats.map(hat => {
          return (
            <tr key={hat.id}>
              <td>
                <img src={hat.picture_url} alt="unavailable" width="100" height="100" />
              </td>
              <td>{ hat.style_name } </td>
              <td>{ hat.fabric }</td>
              <td>{ hat.color }</td>
              <td>{ hat.location.closet_name }</td>
              <td>
                <button type="button" className="btn btn-danger"
                onClick={() => deleteHat(hat.id)}
                >Delete</button>
              </td>
            </tr>
          );
        })}
        </tbody>
      </table>
      <div>
        <a href='http://localhost:3000/hats/new/'><button className="btn btn-primary" type='button'>Add a hat!</button></a>
      </div>
      </>
    );
}

export default HatsList;
