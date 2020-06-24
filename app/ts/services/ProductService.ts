class ProductService {

    importProducts(category_id: string, handler: HandlerFunction): Promise<Product[]> {
        return fetch('https://golden-leaf.herokuapp.com/api/product/category/' + category_id)
            .then(res => handler(res))
            .then(res => res.json())
            .then((data: PartialProduct[]) =>
                data.map(p => new Product(p.id, p.description, p.unit_cost))
            )
            .catch(error => { throw new Error(error) });
    }
}