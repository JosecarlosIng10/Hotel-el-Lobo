<%@ Page Title="" Language="C#" MasterPageFile="~/Principal.Master" AutoEventWireup="true" CodeBehind="Habitaciones.aspx.cs" Inherits="ElLobo.Habitaciones" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="contenidoContextual" runat="server">
</asp:Content>
<asp:Content ID="Content3" ContentPlaceHolderID="contenidoPrincipal" runat="server">
     <asp:FileUpload id="FileUploadControl" runat="server" />
    <asp:Button ID="Button2" runat="server" Text="Cargar" Width="103px" Height="22px" OnClick="Button2_Click" />
    <br />
    <asp:TextBox ID="TextBox1" runat="server" Height="245px" Width="396px" TextMode="MultiLine"></asp:TextBox>
    <br />
    <br />
    <asp:Button ID="Button3" runat="server" Text="Guardar" Width="87px" OnClick="Button3_Click" />
    <br />
    <br />
</asp:Content>
