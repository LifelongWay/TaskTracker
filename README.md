# 🚀 Setup: LocalTunnel Quick Guide

Expose your local server (e.g., Django) publicly with LocalTunnel 🔗

---

### 1️⃣ Run your server

```bash
python manage.py runserver
````

### 2️⃣ Start LocalTunnel

```bash
lt --port 8000
```

Get a URL like:
`https://your-tunnel-name.loca.lt`

---

### 3️⃣ Update Django settings ⚙️

Add your tunnel host to `ALLOWED_HOSTS` in `settings.py`:

```python
ALLOWED_HOSTS = ['your-tunnel-name.loca.lt', 'localhost', '127.0.0.1']
```

**Important:** You also need to add your tunnel URL to `CSRF_TRUSTED_ORIGINS` to avoid CSRF verification errors:

```python
CSRF_TRUSTED_ORIGINS = [
    'https://your-tunnel-name.loca.lt',  # <--- Add your tunnel URL here
]
```

---

### 4️⃣ Get Tunnel Password 🔑

Run on same machine:

```bash
curl https://loca.lt/mytunnelpassword
```

Or visit:
`https://loca.lt/mytunnelpassword`

*This is your public IP and required to access the tunnel.*

---

### 5️⃣ Share 🔄

Share the **URL** + **password** only with trusted users.
Visitors must enter the password to connect.

---

⚠️ **Stop tunnel with Ctrl+C** when done.
Only share with trusted people!

---

> > > > > > > > > >## Questions? Open an issue! 📬

