import { useState, useEffect } from 'react';

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

    return (
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
              <img src={hat.picture_url} alt="unavailable" width="100" height="100" />
              <td>{ hat.style_name } </td>
              <td>{ hat.fabric }</td>
              <td>{ hat.color }</td>
              <td>{ hat.location.section_number }</td>
            </tr>
          );
        })}
        </tbody>
      </table>
    );
}

export default HatsList;
