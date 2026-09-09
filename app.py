import streamlit as st

# ============================================================
# MULTIRAG P2
# Multilingual Government Scheme Discovery & Eligibility
# Frontend Prototype
# ============================================================

st.set_page_config(
    page_title="MultiRAG | Government Scheme Intelligence",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# DARK PROFESSIONAL THEME
# ============================================================

st.markdown(
    """
    <style>

    /* =========================
       GLOBAL
       ========================= */

    .stApp {
        background-color: #070f1d;
        color: #e8eef8;
    }

    .main .block-container {
        max-width: 1400px;
        padding-top: 1.2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3, h4 {
        color: #f5f8fc !important;
        font-weight: 700 !important;
    }

    p {
        color: #9fb1c8;
    }

    hr {
        border-color: #17283f !important;
    }

    /* =========================
       SIDEBAR
       ========================= */

    section[data-testid="stSidebar"] {
        background-color: #091426;
        border-right: 1px solid #172b46;
    }

    section[data-testid="stSidebar"] * {
        color: #dce7f5;
    }

    section[data-testid="stSidebar"] .stRadio label {
        font-size: 0.88rem;
    }

    .brand {
        padding: 0.3rem 0 1rem 0;
    }

    .brand-title {
        color: #f5f8fc;
        font-size: 1.55rem;
        font-weight: 750;
    }

    .brand-subtitle {
        color: #7f9abc !important;
        font-size: 0.72rem;
        line-height: 1.45;
    }

    .sidebar-section {
        color: #4d91df !important;
        font-size: 0.67rem;
        font-weight: 750;
        letter-spacing: 0.12em;
        margin-top: 1rem;
        margin-bottom: 0.35rem;
    }

    /* =========================
       TOP BAR
       ========================= */

    .top-label {
        color: #438fe5 !important;
        font-size: 0.7rem;
        font-weight: 750;
        letter-spacing: 0.2em;
    }

    .top-status {
        color: #7187a2 !important;
        font-size: 0.72rem;
        text-align: right;
    }

    /* =========================
       HERO
       ========================= */

    .hero-title {
        font-size: 2.7rem;
        line-height: 1.08;
        font-weight: 750;
        color: #f5f8fc;
        margin-top: 0.3rem;
    }

    .hero-title span {
        color: #459fff;
    }

    .hero-text {
        max-width: 850px;
        color: #9eb1c9;
        font-size: 0.98rem;
        line-height: 1.6;
        margin-top: 0.8rem;
    }

    /* =========================
       SEARCH
       ========================= */

    .search-label {
        color: #dce7f5;
        font-size: 0.88rem;
        font-weight: 650;
        margin-bottom: 0.35rem;
    }

    .stTextInput input,
    .stTextArea textarea {
        background-color: #0b192c !important;
        color: #edf4fc !important;
        border: 1px solid #24476c !important;
        border-radius: 9px !important;
    }

    .stTextInput input::placeholder,
    .stTextArea textarea::placeholder {
        color: #607995 !important;
    }

    .stTextInput input:focus,
    .stTextArea textarea:focus {
        border-color: #3e91ed !important;
        box-shadow: 0 0 0 1px #3e91ed !important;
    }

    /* =========================
       BUTTONS
       ========================= */

    .stButton > button {
        background-color: #ff5b67 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        min-height: 2.55rem;
        font-weight: 700;
    }

    .stButton > button:hover {
        background-color: #ff6d77 !important;
        color: white !important;
    }

    /* =========================
       METRIC CARDS
       ========================= */

    .metric-box {
        background-color: #0b192c;
        border: 1px solid #183451;
        border-radius: 11px;
        padding: 1.15rem;
        min-height: 125px;
    }

    .metric-label {
        color: #7891ae;
        font-size: 0.69rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        font-weight: 650;
    }

    .metric-number {
        color: #f1f6fc;
        font-size: 1.65rem;
        font-weight: 750;
        margin-top: 0.35rem;
    }

    .metric-description {
        color: #637d9b;
        font-size: 0.7rem;
        margin-top: 0.2rem;
    }

    /* =========================
       CATEGORY CARDS
       ========================= */

    .category-box {
        background-color: #0b192c;
        border: 1px solid #183451;
        border-radius: 10px;
        padding: 1rem;
        min-height: 115px;
    }

    .category-icon {
        font-size: 1.35rem;
    }

    .category-name {
        color: #edf4fc;
        font-size: 0.9rem;
        font-weight: 700;
        margin-top: 0.45rem;
    }

    .category-description {
        color: #7188a3;
        font-size: 0.7rem;
        line-height: 1.35;
        margin-top: 0.25rem;
    }

    /* =========================
       INFO / STATUS
       ========================= */

    .info-box {
        background-color: #0a1a30;
        border: 1px solid #1d4266;
        border-left: 4px solid #3689e6;
        border-radius: 8px;
        padding: 0.9rem 1rem;
        color: #9db4ce;
        font-size: 0.78rem;
        line-height: 1.5;
    }

    .status-box {
        background-color: #0b211a;
        border: 1px solid #20543d;
        border-left: 4px solid #45b879;
        border-radius: 8px;
        padding: 0.9rem 1rem;
        color: #9ed1b7;
    }

    .status-title {
        color: #5fd092;
        font-weight: 750;
    }

    /* =========================
       FOOTER
       ========================= */

    .footer {
        text-align: center;
        color: #536b86;
        font-size: 0.68rem;
        padding-top: 1.5rem;
    }

    /* =========================
       MOBILE
       ========================= */

    @media (max-width: 900px) {

        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero-title {
            font-size: 2rem;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# DEMO DATA
# ============================================================

SCHEMES = [
    {
        "name": "PM-KISAN",
        "government": "Central Government",
        "category": "Agriculture",
        "beneficiary": "Eligible farmer families",
        "benefit": "Income support",
        "description": "Income support for eligible landholding farmer families.",
    },
    {
        "name": "PM Vishwakarma",
        "government": "Central Government",
        "category": "Entrepreneurship",
        "beneficiary": "Traditional artisans and craftspeople",
        "benefit": "Training and credit support",
        "description": "Support for eligible traditional artisans and craftspeople.",
    },
    {
        "name": "PMAY-U 2.0",
        "government": "Central Government",
        "category": "Housing",
        "beneficiary": "Eligible urban households",
        "benefit": "Housing assistance",
        "description": "Housing assistance for eligible urban households.",
    },
    {
        "name": "Rythu Bharosa",
        "government": "Telangana",
        "category": "Agriculture",
        "beneficiary": "Eligible farmers",
        "benefit": "Farmer support",
        "description": "Government support for eligible farmers in Telangana.",
    },
    {
        "name": "Aasara Pensions",
        "government": "Telangana",
        "category": "Social Welfare",
        "beneficiary": "Eligible beneficiary groups",
        "benefit": "Pension assistance",
        "description": "Social security pension support for eligible categories.",
    },
    {
        "name": "Kalyana Lakshmi",
        "government": "Telangana",
        "category": "Women Welfare",
        "beneficiary": "Eligible beneficiaries",
        "benefit": "Marriage assistance",
        "description": "Financial assistance under applicable Telangana welfare rules.",
    },
    {
        "name": "Dr. NTR Vaidya Seva",
        "government": "Andhra Pradesh",
        "category": "Health",
        "beneficiary": "Eligible families",
        "benefit": "Healthcare support",
        "description": "Healthcare support for eligible beneficiaries.",
    },
    {
        "name": "NTR Bharosa Pension",
        "government": "Andhra Pradesh",
        "category": "Social Welfare",
        "beneficiary": "Eligible beneficiaries",
        "benefit": "Pension assistance",
        "description": "Social security support under applicable AP guidelines.",
    },
]


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div class="brand">
            <div class="brand-title">🏛️ MultiRAG</div>
            <div class="brand-subtitle">
                Government Scheme Intelligence
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown(
        '<div class="sidebar-section">DISCOVER</div>',
        unsafe_allow_html=True,
    )

    page = st.radio(
        "Discover",
        [
            "Dashboard",
            "Scheme Search",
            "Eligibility Check",
            "Scheme Catalogue",
        ],
        label_visibility="collapsed",
    )

    st.markdown(
        '<div class="sidebar-section">KNOWLEDGE</div>',
        unsafe_allow_html=True,
    )

    knowledge = st.radio(
        "Knowledge",
        [
            "Government Sources",
            "Recent Updates",
        ],
        label_visibility="collapsed",
    )

    st.markdown(
        '<div class="sidebar-section">PREFERENCES</div>',
        unsafe_allow_html=True,
    )

    language = st.selectbox(
        "Language",
        [
            "English",
            "తెలుగు",
        ],
    )

    region = st.selectbox(
        "Region",
        [
            "All Regions",
            "Central Government",
            "Telangana",
            "Andhra Pradesh",
        ],
    )

    st.markdown(
        '<div class="sidebar-section">SYSTEM STATUS</div>',
        unsafe_allow_html=True,
    )

    st.success("● RAG Engine Ready")
    st.success("● AI Engine Ready")

    st.divider()

    st.caption("MultiRAG P2")
    st.caption("v0.1.0")


# ============================================================
# TOP BAR
# ============================================================

top_left, top_right = st.columns([6, 1])

with top_left:

    st.markdown(
        '<div class="top-label">MULTILINGUAL GOVERNMENT AI</div>',
        unsafe_allow_html=True,
    )

with top_right:

    st.markdown(
        '<div class="top-status">● Prototype</div>',
        unsafe_allow_html=True,
    )

st.divider()


# ============================================================
# DASHBOARD
# ============================================================

if page == "Dashboard":

    st.markdown(
        """
        <div class="hero-title">
            Find Government Schemes<br>
            <span>That Fit You</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="hero-text">
            Ask naturally in English or Telugu. MultiRAG searches
            verified government information and provides preliminary
            eligibility guidance to help citizens discover relevant support.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    # Main search

    query = st.text_input(
        "Search government schemes",
        placeholder=(
            "I am a farmer from Telangana. What schemes can I apply for?"
        ),
        label_visibility="collapsed",
    )

    if st.button(
        "✦  Find Relevant Schemes  →",
        type="primary",
        use_container_width=True,
    ):

        if not query.strip():

            st.warning(
                "Please enter your requirement."
            )

        else:

            st.success(
                "Demo search completed. RAG retrieval will be connected next."
            )

            results = SCHEMES

            if region != "All Regions":

                results = [
                    s for s in results
                    if s["government"] == region
                ]

            st.subheader("Potentially Relevant Schemes")

            for scheme in results[:4]:

                with st.container(border=True):

                    st.caption(
                        f"{scheme['government']}  ·  {scheme['category']}"
                    )

                    st.subheader(
                        scheme["name"]
                    )

                    st.write(
                        scheme["description"]
                    )

                    st.write(
                        f"**Potential benefit:** {scheme['benefit']}"
                    )

    st.caption(
        "Try: Schemes for farmers in Telangana  ·  "
        "Scholarships for students  ·  "
        "Health schemes in Andhra Pradesh"
    )

    st.write("")

    # Metrics

    st.subheader("Scheme Intelligence")

    c1, c2, c3, c4 = st.columns(4)

    metric_data = [
        ("45+", "Government Schemes", "Initial target dataset"),
        ("3", "Regions Covered", "Central · Telangana · Andhra Pradesh"),
        ("2", "Languages Supported", "English · తెలుగు"),
        ("100%", "Official Sources", "Target verified-source coverage"),
    ]

    for col, (number, title, description) in zip(
        [c1, c2, c3, c4],
        metric_data,
    ):

        with col:

            st.markdown(
                f"""
                <div class="metric-box">
                    <div class="metric-label">{title}</div>
                    <div class="metric-number">{number}</div>
                    <div class="metric-description">{description}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")

    # Categories

    st.subheader("Explore by Need")

    categories = [
        ("🌱", "Agriculture", "Farmer support and subsidies"),
        ("🎓", "Education", "Scholarships and education"),
        ("💼", "Employment", "Skills, jobs and livelihood"),
        ("❤", "Health", "Healthcare and insurance"),
        ("🏠", "Housing", "Housing assistance"),
        ("👥", "Women & Child", "Women and child welfare"),
        ("🏢", "MSME", "Business and enterprise"),
        ("🤝", "Social Welfare", "Pensions and financial aid"),
    ]

    row1 = st.columns(4)
    row2 = st.columns(4)

    for col, item in zip(
        row1 + row2,
        categories,
    ):

        icon, title, description = item

        with col:

            st.markdown(
                f"""
                <div class="category-box">
                    <div class="category-icon">{icon}</div>
                    <div class="category-name">{title}</div>
                    <div class="category-description">
                        {description}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")

    # Workflow

    st.subheader("How MultiRAG Works")

    steps = [
        ("01", "Ask", "Ask your question in English or Telugu."),
        ("02", "Retrieve", "Find relevant government information."),
        ("03", "Evaluate", "Check eligibility using verified rules."),
        ("04", "Guide", "Get clear guidance with official sources."),
    ]

    cols = st.columns(4)

    for col, (number, title, description) in zip(
        cols,
        steps,
    ):

        with col:

            with st.container(border=True):

                st.caption(number)

                st.subheader(title)

                st.caption(description)

    st.markdown(
        """
        <div class="info-box">
            <b>Important:</b> MultiRAG provides preliminary guidance.
            Final eligibility decisions are made by the concerned
            government authority.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# SCHEME SEARCH
# ============================================================

elif page == "Scheme Search":

    st.title("Scheme Search")

    st.caption(
        "Search government schemes using natural language."
    )

    query = st.text_area(
        "Your requirement",
        placeholder=(
            "Example: I am a farmer from Telangana "
            "looking for financial support."
        ),
        height=110,
    )

    c1, c2 = st.columns(2)

    with c1:

        category = st.selectbox(
            "Category",
            [
                "All Categories",
                "Agriculture",
                "Education",
                "Health",
                "Housing",
                "Entrepreneurship",
                "Social Welfare",
                "Women Welfare",
            ],
        )

    with c2:

        search_region = st.selectbox(
            "Region",
            [
                "All Regions",
                "Central Government",
                "Telangana",
                "Andhra Pradesh",
            ],
        )

    if st.button(
        "✦  Search Schemes",
        type="primary",
        use_container_width=True,
    ):

        results = SCHEMES

        if category != "All Categories":

            results = [
                s for s in results
                if s["category"] == category
            ]

        if search_region != "All Regions":

            results = [
                s for s in results
                if s["government"] == search_region
            ]

        st.subheader(
            f"{len(results)} Potentially Relevant Schemes"
        )

        for scheme in results:

            with st.container(border=True):

                st.caption(
                    f"{scheme['government']}  ·  {scheme['category']}"
                )

                st.subheader(
                    scheme["name"]
                )

                st.write(
                    scheme["description"]
                )

                st.write(
                    f"**Target beneficiary:** "
                    f"{scheme['beneficiary']}"
                )

                st.write(
                    f"**Potential benefit:** "
                    f"{scheme['benefit']}"
                )


# ============================================================
# ELIGIBILITY CHECK
# ============================================================

elif page == "Eligibility Check":

    st.title("Eligibility Check")

    st.caption(
        "Provide your basic details for preliminary eligibility guidance."
    )

    st.markdown(
        """
        <div class="info-box">
            This is a preliminary assessment only.
            The final eligibility decision is made by the
            concerned government authority.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    selected_scheme = st.selectbox(
        "Select Scheme",
        [
            s["name"]
            for s in SCHEMES
        ],
    )

    st.subheader("Applicant Information")

    left, right = st.columns(2)

    with left:

        age = st.number_input(
            "Age",
            min_value=0,
            max_value=120,
            value=25,
        )

        residence = st.selectbox(
            "State of Residence",
            [
                "Telangana",
                "Andhra Pradesh",
                "Other",
            ],
        )

        occupation = st.selectbox(
            "Occupation",
            [
                "Farmer",
                "Student",
                "Artisan",
                "Self-employed",
                "Worker",
                "Other",
            ],
        )

    with right:

        income = st.number_input(
            "Annual Household Income (₹)",
            min_value=0,
            step=10000,
            value=150000,
        )

        social_category = st.selectbox(
            "Social Category",
            [
                "Not specified",
                "SC",
                "ST",
                "BC",
                "Minority",
                "General",
            ],
        )

        gender = st.selectbox(
            "Gender",
            [
                "Prefer not to say",
                "Female",
                "Male",
                "Other",
            ],
        )

    if st.button(
        "✓  Check Preliminary Eligibility",
        type="primary",
        use_container_width=True,
    ):

        st.markdown(
            """
            <div class="status-box">
                <div class="status-title">
                    ● Potentially Eligible
                </div>
                Demonstration result — production rule engine
                will evaluate verified scheme criteria.
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")

        a, b, c, d = st.columns(4)

        with a:
            st.metric("Age", age)

        with b:
            st.metric("Income", f"₹{income:,.0f}")

        with c:
            st.metric("Residence", residence)

        with d:
            st.metric("Occupation", occupation)

        st.subheader("Assessment")

        st.write(
            f"Selected scheme: **{selected_scheme}**"
        )

        st.write(
            "The production eligibility engine will compare "
            "the applicant profile against structured rules "
            "extracted from official government documents."
        )

        st.warning(
            "Final eligibility is determined by the concerned government authority."
        )


# ============================================================
# SCHEME CATALOGUE
# ============================================================

elif page == "Scheme Catalogue":

    st.title("Scheme Catalogue")

    st.caption(
        "Browse the initial demonstration catalogue."
    )

    results = SCHEMES

    if region != "All Regions":

        results = [
            s for s in results
            if s["government"] == region
        ]

    for scheme in results:

        with st.expander(
            f"{scheme['name']}  ·  {scheme['government']}"
        ):

            st.write(
                scheme["description"]
            )

            st.write(
                f"**Category:** {scheme['category']}"
            )

            st.write(
                f"**Target beneficiary:** "
                f"{scheme['beneficiary']}"
            )

            st.write(
                f"**Potential benefit:** "
                f"{scheme['benefit']}"
            )

            st.caption(
                "Official document, evidence page and application URL "
                "will be connected after dataset ingestion."
            )


# ============================================================
# GOVERNMENT SOURCES
# ============================================================

elif knowledge == "Government Sources":

    st.title("Government Sources")

    st.caption(
        "Source transparency is a core design principle of MultiRAG."
    )

    st.markdown(
        """
        <div class="info-box">
            The production system will display the official government
            department, source document, publication/effective date,
            last verified date, evidence page and application URL
            supporting each answer.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    sources = [
        (
            "🇮🇳 Central Government",
            "Official ministries, departments and scheme portals.",
        ),
        (
            "Telangana",
            "Official Telangana departments and scheme portals.",
        ),
        (
            "Andhra Pradesh",
            "Official Andhra Pradesh departments and scheme portals.",
        ),
    ]

    for title, description in sources:

        with st.container(border=True):

            st.subheader(title)

            st.write(description)


# ============================================================
# RECENT UPDATES
# ============================================================

elif knowledge == "Recent Updates":

    st.title("Recent Updates")

    st.caption(
        "Future module for government scheme change detection."
    )

    with st.container(border=True):

        st.subheader("Source Monitoring")

        st.write(
            "Monitor official government pages and documents "
            "for changes to scheme information."
        )

    with st.container(border=True):

        st.subheader("Version Detection")

        st.write(
            "Detect revised guidelines and preserve previous "
            "versions for traceability."
        )

    with st.container(border=True):

        st.subheader("Controlled Re-ingestion")

        st.write(
            "Updated documents will be processed and indexed "
            "again after verification."
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        MultiRAG P2 · Multilingual Government Scheme Discovery & Eligibility
        · Frontend Prototype
    </div>
    """,
    unsafe_allow_html=True,
)