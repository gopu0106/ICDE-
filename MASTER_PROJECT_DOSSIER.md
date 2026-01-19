# CampusEats Ecosystem: The Master Project Dossier (v3.0)

This document is the definitive technical and functional record of the CampusEats project. It documents the evolution of the "Elite Version," covering all core modules, advanced predictive systems, and high-fidelity administrative tools.

---

## 1. Project Overview & Vision

CampusEats is a premium, QR-driven digital wallet ecosystem designed for modern university environments. It eliminates cash-handling friction, optimizes canteen throughput, and provides students with proactive financial intelligence.

---

## 2. Technical Stack & Architecture

| Layer        | Technology              | Key Implementation                                       |
| :----------- | :---------------------- | :------------------------------------------------------- |
| **Frontend** | React 18 / Tailwind CSS | Glassmorphism V2 UI with Framer Motion animations.       |
| **Backend**  | Flask (Python 3.x)      | Decoupled REST API (Port 5001) with JWT security.        |
| **Database** | SQLite / SQLAlchemy     | Atomic operations with multi-state transaction models.   |
| **Auth**     | JWT-Extended            | Role-Based Access Control (Student, Vendor, Admin).      |
| **Visuals**  | Lucide React / Recharts | Premium iconography and high-fidelity trend forecasting. |

---

## 3. The "Elite Build" Design System

Our design philosophy, **Glassmorphism V2**, focuses on depth, motion, and visual hierarchy.

- **Aesthetics**: `Slate-950` backgrounds, `Emerald-500` accents, and `Blue-600` secondary tones.
- **Motion UX**: Used `framer-motion` for stagger-load entrances, layout transitions, and reactive pulsing.
- **Premium Effects**: Shimmering mesh gradients, bento-grid layouts, and "Laser Scan" payment animations.

---

## 4. Module Deep Dive

### A. Student Intelligence Hub

- **Predictive Balance Engine**: Real-time forecasting panel showing "Projected Balance After Next Meal."
- **Smart Recovery (Top-up)**: Intelligent button logic that appears only when low liquidity meets high meal-density windows.
- **Numerical Tickers**: 500ms counting animations for all balance displays.
- **Quick Actions**: Standardized top-up chips (₹100, ₹500) for friction-less deposits.

### B. Admin "Intel Core" Control Center

- **Elite Analytics**: High-fidelity AreaCharts representing 7-day volume forecasting.
- **Live Event Terminal**: Real-time transaction stream with pop-layout animations.
- **Entity Distribution**: Donut charts for monitoring demographic load (Student vs Vendor vs Admin).
- **Global Export**: One-tap CSV audit generation for financial compliance.
- **Power Directory**: Searchable user management with administrative refund capabilities.

### C. Vendor Transaction Terminal

- **Universal POS**: Tablet-optimized split layout for configuration and scanning.
- **Meal Presets**: One-tap cost assignment for standardized canteen slots.
- **Session Intelligence**: Counters for "Meals Served Today" and "Credits Earned" in the active session.
- **Visual Feedback**: Integrated Toast notifications for payment validation.

---

## 5. Security & Data Integrity

- **Transactional Ledger**: All balance adjustments are paired with an immutable entry in the `transactions` table.
- **Schema Evolution**: Successfully migrated to a multi-state `status` model (Pending, Processing, Success).
- **CORS & JWT**: Hardened API security ensuring requests originate only from the verified frontend.

---

## 6. Access Matrix

| Role        | Default Access                  | Primary Tool                       |
| :---------- | :------------------------------ | :--------------------------------- |
| **Student** | student@test.com / password123  | Digital Wallet & Predictive Panels |
| **Vendor**  | vendor@test.com / password123   | Universal POS & Laser Scanner      |
| **Admin**   | admin@campuseats.com / admin123 | Intel Core Dashboard & Audit Tools |

---

## 7. Development Milestones

1.  **Phase 1**: Core API & JWT Auth established.
2.  **Phase 2**: Glassmorphic UI & Student Dashboard v1.
3.  **Phase 3**: Vendor POS & QR Payment Engine Implementation.
4.  **Phase 4**: Admin Analytics & User Management Suite.
5.  **Phase 5**: Global Standardizations (Toasts, Localized Currency).
6.  **Phase 6 (Elite)**: Predictive Intelligence & Admin Elite Overhaul.

---

**Status**: _Operationally Stable & Fully Verified_
**Author**: _Antigravity AI (Supervising Engineer)_
