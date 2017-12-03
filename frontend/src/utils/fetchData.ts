export default function fetchData(path: string, queries?: object) {
    if (queries) {
        path += '?';
        Object.keys(queries).forEach(key => path += key + '=' + queries[key] + '&');
    }
    return fetch('http://localhost:8000' + path).then((response) => {
        // console.log(response);
        return response.json();
    }).catch((e) => {
        console.log("Error in fetchData!", e);
    })
}