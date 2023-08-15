package repository;

import domain.Product;

public interface ProductCatalog {
    Product getByName(String name);
}
