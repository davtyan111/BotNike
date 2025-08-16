// Modern Admin Panel JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Initialize admin panel
    initAdminPanel();
});

function initAdminPanel() {
    // Setup navigation
    setupNavigation();
    
    // Setup forms
    setupForms();
    
    // Setup tables
    setupTables();
    
    // Setup charts
    setupCharts();
    
    // Setup notifications
    setupNotifications();
}

// Navigation Management
function setupNavigation() {
    const navLinks = document.querySelectorAll('.sidebar-nav a');
    const currentPath = window.location.pathname;
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
}

// Form Management
function setupForms() {
    // Auto-resize textareas
    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(textarea => {
        textarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = this.scrollHeight + 'px';
        });
    });
    
    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    field.classList.add('error');
                    isValid = false;
                } else {
                    field.classList.remove('error');
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                showNotification('Please fill in all required fields', 'error');
            }
        });
    });
    
    // Real-time search
    const searchInputs = document.querySelectorAll('.search-input');
    searchInputs.forEach(input => {
        input.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            const tableRows = this.closest('.table-container').querySelectorAll('tbody tr');
            
            tableRows.forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(searchTerm) ? '' : 'none';
            });
        });
    });
}

// Table Management
function setupTables() {
    // Sortable tables
    const tableHeaders = document.querySelectorAll('.table th[data-sort]');
    tableHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const table = this.closest('table');
            const tbody = table.querySelector('tbody');
            const rows = Array.from(tbody.querySelectorAll('tr'));
            const columnIndex = Array.from(this.parentNode.children).indexOf(this);
            const sortDirection = this.dataset.sort === 'asc' ? 'desc' : 'asc';
            
            rows.sort((a, b) => {
                const aValue = a.children[columnIndex].textContent;
                const bValue = b.children[columnIndex].textContent;
                
                if (isNaN(aValue) || isNaN(bValue)) {
                    return sortDirection === 'asc' 
                        ? aValue.localeCompare(bValue) 
                        : bValue.localeCompare(aValue);
                }
                
                return sortDirection === 'asc' 
                    ? parseFloat(aValue) - parseFloat(bValue) 
                    : parseFloat(bValue) - parseFloat(aValue);
            });
            
            tbody.innerHTML = '';
            rows.forEach(row => tbody.appendChild(row));
            
            this.dataset.sort = sortDirection;
            this.classList.toggle('sort-asc', sortDirection === 'asc');
            this.classList.toggle('sort-desc', sortDirection === 'desc');
        });
    });
    
    // Pagination
    const tables = document.querySelectorAll('.table');
    tables.forEach(table => {
        const tbody = table.querySelector('tbody');
        const rows = tbody.querySelectorAll('tr');
        const rowsPerPage = 10;
        let currentPage = 1;
        
        if (rows.length > rowsPerPage) {
            setupPagination(table, rows, rowsPerPage);
        }
    });
}

// Chart Management
function setupCharts() {
    const chartContainers = document.querySelectorAll('.chart-container');
    
    chartContainers.forEach(container => {
        const chartType = container.dataset.chart;
        const chartData = JSON.parse(container.dataset.chartData || '{}');
        
        if (chartType === 'bar') {
            createBarChart(container, chartData);
        } else if (chartType === 'line') {
            createLineChart(container, chartData);
        } else if (chartType === 'pie') {
            createPieChart(container, chartData);
        }
    });
}

// Notification System
function setupNotifications() {
    // Auto-hide notifications
    const notifications = document.querySelectorAll('.notification');
    notifications.forEach(notification => {
        setTimeout(() => {
            notification.style.opacity = '0';
            setTimeout(() => notification.remove(), 300);
        }, 5000);
    });
}

// Utility Functions
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.opacity = '0';
        setTimeout(() => notification.remove(), 300);
    }, 5000);
}

// Chart Creation Functions
function createBarChart(container, data) {
    const canvas = document.createElement('canvas');
    canvas.width = container.offsetWidth;
    canvas.height = 300;
    container.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    const labels = Object.keys(data);
    const values = Object.values(data);
    
    // Simple bar chart implementation
    const barWidth = canvas.width / labels.length;
    const maxValue = Math.max(...values);
    
    ctx.fillStyle = '#2563eb';
    labels.forEach((label, index) => {
        const barHeight = (values[index] / maxValue) * (canvas.height - 40);
        ctx.fillRect(index * barWidth + 10, canvas.height - barHeight - 20, barWidth - 20, barHeight);
        
        ctx.fillStyle = '#64748b';
        ctx.font = '12px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(label, index * barWidth + barWidth / 2, canvas.height - 5);
    });
}

function createLineChart(container, data) {
    const canvas = document.createElement('canvas');
    canvas.width = container.offsetWidth;
    canvas.height = 300;
    container.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    const labels = Object.keys(data);
    const values = Object.values(data);
    
    // Simple line chart implementation
    const maxValue = Math.max(...values);
    const stepX = canvas.width / (labels.length - 1);
    
    ctx.beginPath();
    ctx.strokeStyle = '#2563eb';
    ctx.lineWidth = 2;
    
    labels.forEach((label, index) => {
        const x = index * stepX;
        const y = canvas.height - (values[index] / maxValue) * (canvas.height - 40);
        
        if (index === 0) {
            ctx.moveTo(x, y);
        } else {
            ctx.lineTo(x, y);
        }
    });
    
    ctx.stroke();
}

function createPieChart(container, data) {
    const canvas = document.createElement('canvas');
    canvas.width = container.offsetWidth;
    canvas.height = 300;
    container.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    const labels = Object.keys(data);
    const values = Object.values(data);
    const total = values.reduce((sum, val) => sum + val, 0);
    
    let currentAngle = 0;
    const colors = ['#2563eb', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6'];
    
    values.forEach((value, index) => {
        const sliceAngle = (value / total) * 2 * Math.PI;
        
        ctx.beginPath();
        ctx.moveTo(canvas.width / 2, canvas.height / 2);
        ctx.arc(canvas.width / 2, canvas.height / 2, 100, currentAngle, currentAngle + sliceAngle);
        ctx.closePath();
        ctx.fillStyle = colors[index % colors.length];
        ctx.fill();
        
        currentAngle += sliceAngle;
    });
}

// Pagination
function setupPagination(table, rows, rowsPerPage) {
    const totalPages = Math.ceil(rows.length / rowsPerPage);
    let currentPage = 1;
    
    function showPage(page) {
        const start = (page - 1) * rowsPerPage;
        const end = start + rowsPerPage;
        
        rows.forEach((row, index) => {
            row.style.display = (index >= start && index < end) ? '' : 'none';
        });
        
        updatePaginationControls(page, totalPages);
    }
    
    function updatePaginationControls(page, totalPages) {
        const pagination = table.querySelector('.pagination') || createPaginationControls(table);
        pagination.innerHTML = '';
        
        for (let i = 1; i <= totalPages; i++) {
            const pageBtn = document.createElement('button');
            pageBtn.textContent = i;
            pageBtn.className = i === page ? 'active' : '';
            pageBtn.addEventListener('click', () => showPage(i));
            pagination.appendChild(pageBtn);
        }
    }
    
    function createPaginationControls(table) {
        const pagination = document.createElement('div');
        pagination.className = 'pagination';
        table.appendChild(pagination);
        return pagination;
    }
    
    showPage(1);
}

// Dashboard Stats
function updateDashboardStats() {
    const stats = {
        totalPhotos: 1250,
        totalLocations: 45,
        totalTariffs: 12,
        totalSubcodes: 8
    };
    
    const statElements = document.querySelectorAll('.stat-number');
    statElements.forEach(element => {
        const target = parseInt(element.dataset.value);
        animateNumber(element, 0, target, 2000);
    });
}

function animateNumber(element, start, end, duration) {
    const range = end - start;
    const increment = range / (duration / 16);
    let current = start;
    
    const timer = setInterval(() => {
        current += increment;
        if (current >= end) {
            current = end;
            clearInterval(timer);
        }
        element.textContent = Math.floor(current);
    }, 16);
}

// Initialize
function initAdminPanel() {
    setupNavigation();
    setupForms();
    setupTables();
    setupCharts();
    setupNotifications();
    updateDashboardStats();
}

// Export for use in other files
window.AdminPanel = {
    showNotification,
    updateDashboardStats,
    initAdminPanel
};
