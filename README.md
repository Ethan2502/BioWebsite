# Ethan's Link-in-Bio

A modern, responsive, and aesthetically pleasing "Link in Bio" landing page. This project features a **Glassmorphism** design style and a custom **Solar Light** color theme.

## ✨ Features

*   **Glassmorphism UI**: Semi-transparent card design with blur effects (`backdrop-filter`).
*   **Solar Light Theme**: A warm, soothing color palette based on extracted tones (Beige, Cream, Dark Brown).
*   **Animated Background**: Subtle, moving mesh gradient that adds life to the page without being distracting.
*   **Responsive**: Looks great on mobile, tablet, and desktop devices.
*   **Performance**: Single-file architecture (`index.html`) for lightning-fast loading.

## 🚀 Setup & Usage

No installation or build process is required!

1.  **Download** or clone this repository.
2.  **Open** `index.html` in any modern web browser (Chrome, Safari, Firefox).
3.  **That's it!**

## 🛠️ Customization

You can personalize everything by editing `index.html`.

### Changing the Profile Picture
Look for the `<img>` tag inside `.container`:
```html
<img src="/path/to/your/image.jpg" alt="Profile Picture" class="profile-pic">
```
*Tip: For best results, place your image in the same folder and use a relative path (e.g., `src="photo.jpg"`).*

### updating Links
Scroll down to the `.links` section and modify the `<a>` tags:
```html
<div class="links">
    <a href="https://your-link.com" target="_blank" class="link-btn">Button Text</a>
    <!-- Add more links here -->
</div>
```

### Modifying Colors
The theme is powered by CSS variables at the top of the `<style>` block:
```css
:root {
    --color-dark: #ddd6c1;  /* Background darker shade */
    --color-mid: #eee8d5;   /* Background medium shade */
    --color-light: #fdf6e3; /* Background lightest shade */
    --text-main: #4a4538;   /* Primary text color */
}
```
Change these hex codes to create your own color scheme.

## 📂 Project Structure

*   `index.html`: The main file containing HTML, CSS, and structural logic.
*   `extract_colors.py`: (Utility) Script used to generate the color palette from a reference image.
