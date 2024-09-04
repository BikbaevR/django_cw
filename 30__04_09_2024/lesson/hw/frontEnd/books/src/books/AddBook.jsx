import {useRef} from "react";

const AddBook = ({domainName}) => {

    const formInput = useRef()

    const getDataFromForm = (event) => {
        event.preventDefault()

        fetch(domainName + 'books/', {
            method: 'POST',
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'name': formInput.current.name.value,
                'author': formInput.current.author.value,
                'year': formInput.current.year.value,
                'price': formInput.current.price.value,
                'count': formInput.current.count.value
            })
        })
            .then(res => res.json())
            .then(response => console.log(response))

    }
    return (
        <div className={'addBook'}>
            <h3>Добавить книгу</h3>
            <div className={'addBookForm'}>
                <form onSubmit={getDataFromForm} ref={formInput}  className={'form'}>
                    <input type={'text'} name={'name'} placeholder={'Name'} required />
                    <input type={'text'} name={'author'} placeholder={'Author'} required />
                    <input type={'number'} name={'year'} placeholder={'Year'} required />
                    <input type={'number'} name={'price'} placeholder={'Price'} required />
                    <input type={'number'} name={'count'} placeholder={'Count'} required />
                    <button>Добавить книгу</button>
                </form>
            </div>
        </div>
    )
}

export default AddBook