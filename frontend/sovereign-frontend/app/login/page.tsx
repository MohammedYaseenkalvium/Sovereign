export default function LoginPage(){
    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-100">
            <div className="bg-white p-8 rounded shadow-md w-96">
                <h1 className="text-2xl font-bold mb-4">Sign In</h1>
                <input 
                    type="email"
                    placeholder="Email"
                    className="w-full mb-4 p-2 border rounded"
                />

                <input
                    type="password"
                    placeholder="Password"
                    className="w-full mb-4 p-2 border rounded"
                />

                <button className="w-full bg-indigo-600 text-white py-2 rounded">
                    Sign In
                </button>
            </div>
        </div>
    );
}