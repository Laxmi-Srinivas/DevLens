import { SquareCode } from 'lucide-react';
function Navbar() {
    const links = [
        {
            title: "Features",
            href: "#features",
        },
        {
            title: "How It Works",
            href: "#how-it-works",
        },
        {
            title: "Pricing",
            href: "#pricing",
        },
        {
            title: "Testimonials",
            href: "#testimonials",
        },
        {
            title: "About",
            href: "#about",
        },
    ];
  return (
    <nav className="flex justify-between items-center py-6 px-10">
      <div className=" brand-section flex items-center gap-2">
        <SquareCode size={20} strokeWidth={1} absoluteStrokeWidth />
        <h2 className="font-['Saira']">DevLens</h2>
      </div>

      <ul className="links flex gap-8">
        {
            links.map((link)=>{
                return(
                    <li key={link.title}>
                        <a href={`#${link.href}`}>{link.title}</a>
                    </li>
                );
            })
        }
      </ul>

      <div className="buttons flex gap-4">
        <button>Sign In</button>
        <button>Get Started</button>
      </div>
    </nav>
  );
}

export default Navbar;