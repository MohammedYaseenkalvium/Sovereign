export default function Dashboard(){
  return(
    <div className="flex">
      <aside className="w-64 h-screen bg-gray-100 p-4">
        Sidebar
      </aside>

      <main className="flex-1 p-6">
        <h1 className="text-3xl font-bold">
          Governance Dashboard
          </h1>
      </main>
    </div>
  )
}