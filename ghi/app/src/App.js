import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import HatsList from './HatsList';
import ShoesList from './ShoesList';

function App(props) {
  console.log(props)
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="shoes">
            <Route path="" element={<ShoesList />} />
          </Route>
          <Route path="hats">
            <Route path="" element={<HatsList />} />
          </Route>
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
