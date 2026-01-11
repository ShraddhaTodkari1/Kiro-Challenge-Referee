
def referee_logic(choice):
    comparison = {
        "React": {
            "Pros": "Complete flexibility, massive ecosystem, client-side rendering.",
            "Cons": "Manual SEO setup, slower initial page load, requires more configuration.",
            "Best For": "Single-page applications (SPAs) where SEO isn't the priority."
        },
        "Next.js": {
            "Pros": "Built-in SEO, Server-Side Rendering (SSR), faster performance out of the box.",
            "Cons": "Stricter structure, larger bundle size, steeper learning curve for beginners.",
            "Best For": "E-commerce or Blogs where Google search ranking is critical."
        }
    }

    if choice in comparison:
        data = comparison[choice]
        print(f"\n--- Analysis for {choice} ---")
        print(f"✅ Pros: {data['Pros']}")
        print(f"❌ Cons: {data['Cons']}")
        print(f"💡 Verdict: {data['Best For']}")
    else:
        print("Technology not found in database.")


print("Welcome to the Week 6 Referee Tool")
user_choice = input("Enter 'React' or 'Next.js' to see the trade-offs: ")
referee_logic(user_choice)
