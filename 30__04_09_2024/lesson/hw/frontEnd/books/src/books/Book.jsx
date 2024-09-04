

const Book = ({book}) => {
    return (
        <div className="book">
            <p>Название: {book.name}</p>
            <p>Автор: {book.author}</p>
            <p>Год: {book.year}</p>
            <p>Цена: {book.price}</p>
            <p>Кол-во: {book.count}</p>
        </div>
    )
}

export default Book