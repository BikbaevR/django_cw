import Book from './Book.jsx'
import {useEffect, useState} from "react";


const GetBooks = ({domainName}) => {
    const [result, setResult] = useState([])
    useEffect(() => {
        fetch(domainName + 'books', {
            method: 'GET',
            headers: {
                'Accept': 'application/json'
            }
        })
            .then(response => response.json())
            .then(res=>{
                setResult(res)
            });
    }, []);


    return (
        <div className={'bookContainer'}>
            <h3>Книги</h3>
            <div className={'books'}>

                {
                    result.map((e) => {
                        return <Book key={e.id} book={e}/>
                    })
                }
            </div>

        </div>

    )
}

export default GetBooks