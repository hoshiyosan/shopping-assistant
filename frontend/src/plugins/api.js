import http from './http'

export class APIObject {
    constructor(object, baseURI) {
        this.object = object;
        this.baseURI = baseURI;
    }

    get(objectUID) {
        return new Promise((resolve, reject) => {
            http.get(`${this.baseURI}/${objectUID}`)
                .then(response => resolve(response.data))
                .catch(() => reject(`Unable to retrieve ${this.object}`));
        })
    }

    search(query) {
        return new Promise((resolve, reject) => {
            http.get(`${this.baseURI}?q=${query}`)
                .then(response => resolve(response.data))
                .catch(() => reject(`Search request for ${this.object} failed`));
        })
    }

    create(objectData) {
        return new Promise((resolve, reject) => {
            http.post(`${this.baseURI}`, objectData)
                .then(response => resolve(response.data))
                .catch(() => reject(`Unable to create ${this.object} with data ${objectData}`));
        })
    }

    update(objectData) {
        objectData = Object.assign({}, objectData);
        const objectUID = objectData._id;
        delete objectData._id;

        return new Promise((resolve, reject) => {
            http.put(`${this.baseURI}/${objectUID}`, objectData)
                .then(response => resolve(response.data))
                .catch(() => reject(`Unable to update ${this.object} with data ${objectData}`));
        })
    }

    delete(objectUID) {
        return new Promise((resolve, reject) => {
            http.delete(`${this.baseURI}/${objectUID}`)
                .then(response => resolve(response.data))
                .catch(() => reject(`Unable to delete ${this.object}`));
        })
    }
}
