export default async function getRates(): Promise<any> {
    try {
        const response = await fetch('http://localhost:5000/all-rates/');
        return await response.blob();
    } catch (e) {
        console.log("Error!!!");
    }
}