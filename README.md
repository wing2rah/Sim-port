# 📱 SIM Port Details Manager

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat&logo=supabase&logoColor=white)](https://supabase.com)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

> A sleek and modern web application for managing SIM card porting details between different telecom providers.

![Project Preview](https://via.placeholder.com/800x400?text=SIM+Port+Details+Manager)

## ✨ Features

- 📝 Record SIM porting details with ease
- 🔄 Track transitions between multiple telecom providers
- 🔒 Secure data storage with Supabase
- 📱 Responsive design for all devices
- 🎨 Modern UI with glassmorphism effects
- 🔐 Password-protected data retrieval

## 🚀 Tech Stack

- **Frontend:**
  - HTML5
  - CSS3 (with Custom Properties)
  - Vanilla JavaScript
  - Google Fonts (Poppins)

- **Backend & Database:**
  - Supabase (PostgreSQL)
  - Supabase JavaScript Client

- **Design:**
  - Glassmorphism UI
  - Responsive Layout
  - CSS Grid & Flexbox
  - Custom animations

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sim-port-details.git
cd sim-port-details
```

2. Configure Supabase:
   - Create a new project on [Supabase](https://supabase.com)
   - Create a table named `datasim` with the following columns:
     - `phoneNumber` (text)
     - `simNumber` (text)
     - `date` (date)
     - `from` (text)
     - `to` (text)
   - Update the `SUPABASE_URL` and `SUPABASE_API_KEY` in the script

3. Open `index.html` in your browser or deploy to your preferred hosting service.

## 💻 Usage

1. **Adding a New Record:**
   - Fill in all required fields
   - Click the "Add" button
   - Confirmation message will appear

2. **Viewing Records:**
   - Click the "Fetch" button
   - Enter the password when prompted
   - Records will display in a list format

3. **Deleting Records:**
   - Enter the phone number
   - Click the "Delete" button
   - Confirmation message will appear

## 🔐 Security Features

- Password-protected data retrieval
- Secure database connections
- Environment variables for sensitive data

## 📱 Responsive Design

The application is fully responsive and optimized for:
- Desktop computers
- Tablets
- Mobile phones

## 🎨 Customization

### Color Scheme
```css
:root {
    --primary-color: #6366f1;
    --primary-dark: #4f46e5;
    --secondary-color: #f8fafc;
    --text-color: #1e293b;
    --border-radius: 12px;
}
```

## 📝 Database Schema

```sql
CREATE TABLE datasim (
    id SERIAL PRIMARY KEY,
    phoneNumber TEXT NOT NULL,
    simNumber TEXT NOT NULL,
    date DATE NOT NULL,
    from TEXT NOT NULL,
    to TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW())
);
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contact

rahul shah - [@wing2rah](https://twitter.com/wing2rah) - wing2rah@gmail.com

Project Link: [see project](https://github.com/wing2rah/Sim-port)

## 🙏 Acknowledgments

- [Supabase](https://supabase.com) for the amazing backend service
- [Google Fonts](https://fonts.google.com) for the Poppins font family
- [Simple Icons](https://simpleicons.org) for the tech stack icons

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/wing2rah">RAHUL SHAH</a>
</p>
