export default async function getRates() {
    try {
        const response = await fetch('http://localhost:5000/all-rates/');
        console.log(response.blob());
    } catch (e) {
        console.log("Error!!!");
    }
}
