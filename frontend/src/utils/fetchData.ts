export default function fetchData() {
    return fetch('http://localhost:8000/all-companies/').then((response) => {
        console.log(response.json());
        return response.json();
    }).catch((e) => {
        console.log("Error!!!", e);
    })
}